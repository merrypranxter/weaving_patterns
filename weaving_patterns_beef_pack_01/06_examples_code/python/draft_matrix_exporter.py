import csv

def plain_weave(w,h):
    return [[(x+y)%2 for x in range(w)] for y in range(h)]

def twill(w,h,float_len=4,step=1):
    return [[1 if ((x+y*step)%float_len)<float_len/2 else 0 for x in range(w)] for y in range(h)]

def save_csv(matrix, path):
    with open(path,'w',newline='') as f:
        csv.writer(f).writerows(matrix)

if __name__ == '__main__':
    save_csv(twill(32,32), 'twill_32.csv')
