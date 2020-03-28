#!/usr/bin/env python3
#pylint: disable=invalid-name
#pylint: disable=missing-function-docstring
#pylint: disable=unused-argument
"""
Command line utility to extract signals or description
from a range of Rigol Oscilloscope waveform file.

Use like this::

    wfmconvert 1102E info DS1102E-A.wfm
    wfmconvert 1102E csv DS1102E-A.wfm
    wfmconvert 1102E wav DS1102E-A.wfm

"""
import os
import sys
import argparse

import RigolWFM.wfm as rigol

def info(args, scope_data, infile):
    s = scope_data.describe()
    print(s)

def csv(args, scope_data, infile):
    csv_name = os.path.splitext(infile)[0] + '.csv'

    if os.path.isfile(csv_name) and not args.force:
        print("'%s' exists, use --force to overwrite" % csv_name)
        return

    s = scope_data.csv()
    with open(csv_name, 'wb') as f:
        b = s.encode(encoding='utf-8')
        f.write(b)

def wav(args, scope_data, infile):

    wav_name = os.path.splitext(infile)[0] + '.wav'
    if os.path.isfile(wav_name) and not args.force:
        print("'%s' exists, use --force to overwrite" % wav_name)
        return

    scope_data.wav(wav_name, channel=args.channel)

def main():

    parser = argparse.ArgumentParser(
        prog='wfmconvert',
        description='Parse Rigol WFM files.',
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        '--force',
        action='store_true',
        help="overwrite existing csv or wav files"
    )

    parser.add_argument(
        '--channel',
        type=int,
        default=1,
        help="designate channel to save in .wav file"
    )

    parser.add_argument(
        'model',
        type=str,
        help='the type of scope that created the WFM file' + rigol.valid_scope_list()
    )

    parser.add_argument(
        dest='action',
        choices=['csv', 'info', 'wav'],
        help="Action to perform on the WFM file"
    )

    parser.add_argument(
        'infile',
        type=str,
        nargs='+',
        help="Input WFM file"
    )

    args = parser.parse_args()

    actionMap = {"info": info, "csv": csv, "wav": wav}

    for filename in args.infile:
        try:
            scope_data = rigol.Wfm.from_file(filename, args.model)
            actionMap[args.action](args, scope_data, filename)

        except rigol.Parse_WFM_Error as e:
            print("Format does not follow a known format.", file=sys.stderr)
            print("To help development, post report this error\n", file=sys.stderr)
            print("as an issue to https://github.com/scottprahl/RigolWFM\n", file=sys.stderr)
            print(e, file=sys.stderr)
            sys.exit()

if __name__ == "__main__":
    main()