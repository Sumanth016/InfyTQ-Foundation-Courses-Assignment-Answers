//Can store homogeneous data
list_of_airlines=["AI","EM","BA"]
console.log("List of airlines:"+ list_of_airlines)
//Can  store heterogeneous data
sample_list=["Mark",5,"Jack",9, "Chan",5]
console.log("Sample List:"+sample_list)
//Length 
console.log("Number of elements:"+sample_list.length)
//Random read
console.log("Element at 2nd index position:"+ sample_list[2])
//Random write
sample_list[2]="James"
//Random read
console.log("Element at 2nd index position after random write:"+sample_list[2])
//Adding an element
sample_list.push("James")
console.log("After adding an element:"+sample_list)
//Sequential access
for (i=0; i < sample_list.length;i++)
{
console.log(sample_list[i])
}
