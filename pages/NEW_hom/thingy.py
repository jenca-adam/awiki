from PIL import Image, ImageDraw
import itertools
import random
import sys
class Thingy:
    def __init__(self, n, s):
        self.n=n
        self.s=s
    def __invert__(self):
        s=self.s
        if set() in self.s:
            self.s.remove(set())
        else:
            self.s.append(set())
        if set(range(1,self.n+1)) in self.s:
            self.s.remove(set(range(1,self.n+1)))
        else:
            self.s.append(set(range(1,self.n+1)))
        return Thingy(self.n, s)
    def __matmul__(self, ot):
        n= self.n+ot.n
        r=[]
        for a in ot.s:
            a_shifted = {i+self.n for i in a}
            if a_shifted not in r:
                r.append(a_shifted)
        unified = [a.union(b) for (a,b) in itertools.product(self.s, r)]
        return Thingy(n, unified)

def diagram(sets, width, height):
    img = Image.new("RGB",(width, height))
    img.paste((255,255,255),(0,0,width,height))
    imgd = ImageDraw.ImageDraw(img)
    levels = [(a,list(b)) for a, b in itertools.groupby(sorted(sets,key=len),key=len)]
    n = len(levels)
    children = {}
    offsets = {}
    for i, level in enumerate(levels):
        _,level = level
        k=len(level)
        print(i,n)
        for j, s in enumerate(level):
            if (i,j) not in offsets:
                offsets[i,j]=random.randint(-width//100, width//100)
            sp = (0.5+(j-(k-1)/2)/k)*width, (0.5-(i-(n-1)/2)/n)*height
            print("s",sp,j,k,i,n)
            
            parents = []
            for ii, hl in enumerate(levels[i+1:]):
                _, hl = hl
                kk = len(hl)
                ii += i +1
                print(ii,n)
                for jj, hs in enumerate(hl):
                    if (ii,jj) not in offsets:
                        offsets[ii,jj]=random.randint(-width//100, width//100)
                    hsp = (0.5+(jj-(kk-1)/2)/kk)*width, (0.5-(ii-(n-1)/2)/n)*height
                    print("hs",hsp)
                    if hs.issuperset(s):
                        for parent in parents:
                            if hs.issuperset(parent):
                                break
                        else:
                            parents.append(hs)
                            imgd.line((*sp, *hsp), (0,0,0), max(1,width//500))
                            if (ii,jj) not in children:
                                children[(ii,jj)]=set()
                            children[(ii,jj)].update(s)
            imgd.circle(sp,width/30,(125,125,255))
            imgd.text(sp, repr(s-children.get((i,j),set())),(0,0,0), font_size=width/40, anchor="mm")
    return img

def parse_input(input_stream):
    context = {}
    while True:
        name = input_stream.readline().strip()
        if name=="END":
            break
        n=int(input_stream.readline().strip())
        s=list(map(eval,input_stream.readline().strip().replace("{}","set()").split(";")))
        context[name]=Thingy(n,s)
        input_stream.readline()
    template = input_stream.readline().strip()
    ev = eval(template, context)
    return ev

def main():
    if len(sys.argv)>=3:
        input_name=sys.argv[1]
        output_name = sys.argv[2]
    elif len(sys.argv)==2:
        input_name=sys.argv[1]
        output_name = None
    else:
        print("need more args", file=sys.stderr)
        exit(1)
    ev = parse_input(open(input_name,'r'))
    img = diagram(ev.s, 2048, 2048)
    print("\n\n---\nRESULT:")
    print(ev.s)
    if output_name is not None:
        img.save(output_name)
    img.show()
if __name__=="__main__":
    main()
