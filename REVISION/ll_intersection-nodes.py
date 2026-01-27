class IntersectionNode:
        def solution(self,list1,list2):
            p1=list1
            p2=list2

            while p1!=p2:
                p1= p1.next if p1 else list2
                p2= p2.next if p2 else list1

            if p1==p2:
                return p1
            else:
                return None
        
ob = IntersectionNode()
print("Intersection at node: ",ob.solution([1,2,6,7,8],[3,4,5,6,7,8]))