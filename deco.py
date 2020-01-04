# -*- coding: utf-8 -*-
import argparse
import sys
from os.path import basename, splitext
from base64 import b64decode

def decodeb64(code):
    try:
        return b64decode(code)
    except Exception as e:
        print("[x] decodeb64() err ->", e)
        exit(1)

def read_text(file_name):
    try:
        with open(file_name, "r") as f:
            d = f.read().strip()
    except Exception as e:
        print("[x] read_text() err ->", e)
        exit(1)
    return d

def write_text(code, file_name, mode="w"):
    try:
        with open(file_name, mode) as f:
            f.write(code)
    except Exception as e:
        print("[x] write_text() err ->", e)
        exit(1)

def str_decode(code, charcode):
    try:
        return code.decode(charcode)
    except Exception as e:
        print("[x] str_decode() err ->", e)
    return code

def extract_ioc(code):
    try:
        from cyobstract import extract
    except ImportError:
        print("[x] git clone https://github.com/cmu-sei/cyobstract.git\npython setup.py install")
        exit(1)
    return [(k, v) for k, v in extract.extract_observables(code).items() if len(v) != 0]

def ungzip(filename):
    import gzip
    try:
        with gzip.open(filename, mode="rt") as f:
            d = f.read()
    except Exception as e:
        print("[x] ungzip() err ->", e)
        exit(1)
    return d

def main():
    parser = argparse.ArgumentParser(
        prog="PowerShell Decoder",
        usage="Python3 " + basename(sys.argv[0]) + " args ...",
        description="Sample:\n" + basename(sys.argv[0])+" -f hoge.txt -o out.gzip -i",
        epilog="end",
        add_help=True,
    )
    parser.add_argument("-d", "--decode", help="Base64 String")
    parser.add_argument("-f", "--file", help="Base64 String From File")
    parser.add_argument("-c", "--charcode", help="Character code. Default is UTF-16", default="UTF-16")
    parser.add_argument("-o", "--output", help="Output FileName")
    parser.add_argument("-g", "--ungzip", help="Unpack gzip. Must -o option", action="store_true", default=False)
    parser.add_argument("-i", "--ioc", help="Extract IoC", action="store_true", default=False)

    args = parser.parse_args()

    if args.decode is args.file is None:
        print("[x] Requre option -d or -f")
        exit(1)
    
    if args.file is not None:
        args.decode = read_text(args.file)
    # decoding
    decode = str_decode(code=decodeb64(args.decode), charcode=args.charcode)

    # Output txt
    if args.output is not None and args.ungzip is False:
        # Write Decoded Base64
        write_text(code=decode, file_name=args.output)
        print("[+] Success Output Base64 Decoded File ->", args.output)
    
    # Output gzip
    if args.ungzip is True and args.output is not None:
        # Write gzip
        write_text(code=decode, file_name=args.output, mode="wb")
        print("[+] Success Output Base64 Decoded File ->", args.output)

        # ungzip
        ungzip_code = ungzip(args.output)
        write_text(ungzip_code, args.output+".txt")
        print("[+] Success Write Ungzip Code")
        print("[+] Success Output Ungzip Code")
        print(ungzip_code)

    # Extract IoC
    if args.ioc:
        print("[+] Print IoC")
        if args.ungzip is True:
            for val in extract_ioc(ungzip_code):
                print(val[0], "->", ",".join(list(val[1])))
        else:
            for val in extract_ioc(decode):
                print(val[0], "->", ",".join(list(val[1])))

    # print Decoded Base64
    print("[+] Output Base64 Decoded")
    print(decode)

if __name__ == '__main__':
    main()
