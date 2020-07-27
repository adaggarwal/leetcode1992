class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #initialize the  two variables required
        stk = []
        waterCollected = 0

        #iterate over the whole array of bars
        for i in range(0,len(height)):

            #while there is something  in the stack and the current bar's height is more than 
            #the height of index of the stack's top value
            while stk and height[i] > height[stk[-1]]:

                #let's pop the top of the stack and call this index as top
                top = stk.pop()

                #check if the last pop results in underflow --> break 
                if not len(stk):
                    break

                #calculate the distance from current bar to the top of the stack's element index
                #remember this is different from the element we popped; due to the while loop
                # we are trying to touch all the elements in the stack which are smaller than current
                distance = i - stk[-1] - 1

                #now find out the water collected between the current and stack's last 
                #element index's height--> only the minimum of these two will help us 
                #determine the water collected. Again, we need not worry about the bars in 
                #between as they were already covered in the while loop. We're concerned with 
                #two bars here, the distance between them and the water trapped between them 
                #and above the height of top element's height. 
                waterBetweenBars = min(height[i], height[stk[-1]]) - height[top]

                #add each iterative waterBetweenBars collected to the result
                waterCollected += distance*waterBetweenBars 

            #if the height of the current bar is less than or equal to height[stk[-1]]
            #add that index to the stack
            stk.append(i)

        #return the default value or whatever was calculated
        return waterCollected
