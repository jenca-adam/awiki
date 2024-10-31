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
def get_ppos(i,j,k,n,width,height,offsets):
    return (0.5+(j-(k-1)/2)/k)*width+offsets[i,j], (0.5-(i-(n-1)/2)/n)*height

def diagram(sets, width, height):
    img = Image.new("RGB",(width, height))
    img.paste((255,255,255),(0,0,width,height))
    imgd = ImageDraw.ImageDraw(img)
    levels = [(a,list(b)) for a, b in itertools.groupby(sorted(sets,key=len),key=len)]
    n = len(levels)
    children = {}
    connections = {}
    offsets = {}
    positions = {}
    removed=set()
    sets={}
    for i, level in enumerate(levels):
        _,level = level
        k=len(level)

        for j, s in enumerate(level):
            connections[(i,j)]=set()
            if (i,j) not in offsets:
                offsets[i,j]=random.randint(-width//100, width//100)
            sp = get_ppos(i,j,k,n,width,height,offsets) 
            positions[(i,j)]=sp
            parents = []
            for ii, hl in enumerate(levels[i+1:]):
                _, hl = hl
                kk = len(hl)
                ii += i +1
                for jj, hs in enumerate(hl):
                    if (ii,jj) not in offsets:
                        offsets[ii,jj]=random.randint(-width//100, width//100)
                    if hs.issuperset(s):
                        for parent in parents:
                            if hs.issuperset(parent):
                                break
                        else:
                            parents.append(hs)
                            if (i,j) not in connections:
                                connections[(i,j)]=set()
                            connections[(i,j)].add((ii,jj))
                            if (ii,jj) not in children:
                                children[(ii,jj)]=set()
                            children[(ii,jj)].update(s)
            if s and not s-children.get((i,j),set()):
                print("REMOVE",s)
                removed.add((i,j))
            sets[(i,j)]=s
    for node, neighbors in connections.items():
        if node in removed:
            continue
        for nb in neighbors:
            if nb in removed:
                continue
            imgd.line((*positions[node], *positions[nb]),(0,0,0),max(1,width//500))
        
        s=sets[node]
        sp=positions[node]
        imgd.circle(sp,width/30,(125,125,255))     
        imgd.text(sp, repr(s-children.get(node,set())),(0,0,0), font_size=width/40, anchor="mm")

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
    print("\n\n---\nRESULT:")
    print(ev.s)

    img = diagram(ev.s, 4096,4096)

    if output_name is not None:
        img.save(output_name)
    img.show()
if __name__=="__main__":
    main()
