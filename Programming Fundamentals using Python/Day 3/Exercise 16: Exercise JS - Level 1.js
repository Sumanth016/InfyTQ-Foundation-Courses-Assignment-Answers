
num1=5
num2=10
    if(num1 > num2)
       greater = num1
   else
       greater = num2
   while(1)
       {
        if((greater % num1 === 0) && (greater % num2 === 0))
          { 
            lcm = greater
            break;
          }
        greater += 1
       }
    console.log(lcm)
//Write your code here
