def encode_url_args(args):
    return '?'+'&'.join(['='.join(x) for x in args.items()])
