package main
import (
    "fmt"
)
func main(){
    //Creating an array of fixed size
    var ticketArray=[5] int {78808, 26302, 0, 13503, 48306}
  
    var i int=0

    //Random Read
    fmt.Println("Element at 2nd index position:")
    fmt.Println(ticketArray[2])

	//Random Write
	ticketArray[2]=93634

	//Random Read
    fmt.Println("Element at 2nd index position after random write:")
    fmt.Println(ticketArray[2])

    //To access the elements in the array sequentially
    fmt.Println("Elements in array are:")
    for i=0; i < len(ticketArray); i++{
       fmt.Println(ticketArray[i])
    }
}
