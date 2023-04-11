#야근의 피로도 최소화 프로그램
import heapq

def fatigueRate(n, works):
    result = 0
    
    pq = []
    for work in works:
        heapq.heappush(pq, -work)
    
    for i in range(n):
        work = heapq.heappop(pq)
        if work == 0:
            return 0
        heapq.heappush(pq, work+1)
        print(pq)
    for work in pq:
        result += work ** 2
        
    for i in range(len(pq)):
        pq[i] *= -1

    return pq, result

Works = [int(n) for n in input("enter work load >> ").split()]
N = int(input("enter the remaining work times >> "))

Result = fatigueRate(N, Works)
print(Result[0], Result[1])


#이진탐색트리 삭제 코드
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class Bst:
    def __init__(self):
        self.root = None

    def bst_insert(self, root, key):
        if root == None:
            return Node(key)
        if root.key > key:
            root.left = self.bst_insert(root.left, key)
        elif root.key < key:
            root.right = self.bst_insert(root.right,key)
        else:
            root.value = key
        return root

    def bst_create(self, key):
        self.root = self.bst_insert(self.root, key)

    def bst_remove(self, key):
        self.root, remove = self.remove_f(self.root, key)
        remove.left = remove.right = None
        return remove

    def remove_f(self, t, key):
        if t is None:
            return None, None
        elif key > t.key:
            t.right, r_node = self.remove_f(t.right, key)
        elif key < t.key:
            t.left, r_node = self.remove_f(t.left,key)
        #삭제대상 노드의 자식개수의 종류에 따른 삭제방법 코드 작성
        else:
            if not t.left and not t.right:
                r_node = t
                t = None
            elif not t.right:
                r_node = t
                t = t.left
            elif not t.left:
                r_node = t
                t = t.right
            else:
                replace = t.left
                while replace.right:
                    replace = replace.right
                t.key, replace.key = replace.key, t.key
                t.left, r_node = self.remove_f(t.left, replace.key)
        return t, r_node

    def inorder(self,n):
        if n.key != None:
            if n.left:
                self.inorder(n.left)
        print(str(n.key), ' ' , end='')
        if n.right:
            self.inorder(n.right)


if __name__ == "__main__":
    bst = Bst()
    base = [int(n) for n in input("enter numbers >> ").split()]
    for i in range(len(base)):
        bst.bst_create(base[i])
    
    bst.inorder(bst.root)

    num = int(input("\nenter the number which has to be deleted >> "))

    bst.bst_remove(num)

    bst.inorder(bst.root)