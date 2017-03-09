#!/usr/bin/env python
"""Evaluation Protocol for the ICDAR 2017 Writer Identification Competition on
Historical Data

This script evaluates the results submitted to ScriptNet

"""
import logging

__author__ = "Stefan Fiel"
__copyright__ = "Copyright 2017, Computer Vision Lab, TU Wien"
__credits__ = "Stefan Fiel"
__license__ = "GPLv3"
__version__ = "0.1"
__maintainer__ = "Stefan Fiel"
__email__ = "fiel@caa.tuwien.ac.at"
__status__ = "Production"

OUTPUT_NAME = "Historical-WI Evaluation"

logging.basicConfig(level=logging.INFO, format=OUTPUT_NAME +
                    ' %(levelname)s %(message)s')

logger = logging.getLogger()


def parseGTFile(gtfile):
    import re

    file = open(gtfile, "r")

    gt = {}
    writer = {}
    for line in file:
        line = line.rstrip('\n')
        s = line.split('=')
        if len(s) != 2:
            logger.error('syntax of GT file incorrect: ' + line)
            exit(-2)
        gt[s[0]] = s[1]
        w = re.split('_|-', s[1])
        if len(w) == 0:
            logger.error('syntax of GT file incorrect: ' + line)
            exit(-3)

        writer[s[0]] = w[0]
    file.close()
    return gt, writer


def evaluate(writer, resultfile):
    file = open(resultfile, "r")

    page_count = 0
    top1_count = 0

    average_precision = []
    for line in file:

        line = line.rstrip()
        imgs = line.split(',')

        ref_page = imgs.pop(0)

        if ref_page not in writer:
            logger.error('filename \"' + ref_page + '\" unkown')
            exit(-4)

        ref_writer = writer[ref_page]
        logger.debug("ref_writer:" + ref_writer + " ref_page:" + ref_page)
        if ref_writer == writer[imgs[0]]:
            top1_count = top1_count + 1
        i_count = 0
        i_true = 0
        cur_sum = 0
        for i in imgs:
            i_count = i_count + 1
            if writer[i] == ref_writer:
                i_true = i_true + 1
                cur_sum = cur_sum + (float)(i_true)/i_count

        page_count = page_count + 1
        average_precision.append((float)(cur_sum)/i_true)

    file.close()
    logger.debug("top1_count:" + str(top1_count))
    logger.debug("page_count:" + str(page_count))
    precision = (float)(top1_count)/page_count
    print("len avg:" + str(average_precision))
    meanap = float(sum(average_precision))/float(len(average_precision))
    return precision, meanap

if __name__ == "__main__":
    import argparse
    import os.path

    logger.setLevel(logging.ERROR)
    logger.debug("starting")
    parser = argparse.ArgumentParser(
        description='evaluation the result files submitted via ScriptNet ' +
        'of the ICDAR 2017 Historic-WI')

    parser.add_argument('gtfile', metavar='[GT file]', help='' +
                        'GroundTruth file of the competition with mapping' +
                        '[obfuscated filename]=[real filename]. Real ' +
                        'Filename must look like [writerId]_....')
    parser.add_argument('resultfile', metavar='[result file]', help='' +
                        'Result file submitted for 2017 Historical-WI')

    args = parser.parse_args()

    if not os.path.isfile(args.gtfile):
        logger.error("GT file does not exist!")
        exit(-1)
    else:
        gt, writer = parseGTFile(args.gtfile)

    if not os.path.isfile(args.resultfile):
        logger.error("result file does not exist!")
        exit(-1)
    else:
        precision, meanap = evaluate(writer, args.resultfile)
        logger.info("precision:" + str(precision))
        logger.info("map:" + str(meanap))
        print(precision)
        print(meanap)
