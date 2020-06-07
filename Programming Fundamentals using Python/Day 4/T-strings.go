package main

import (
    "fmt"
)

func main(){
    //Creating a string
    var pancardNumber string="AABGT6715H"

    //To find out the length of the string
    fmt.Println("Length of the PAN card number:", len(pancardNumber))

    //To concatenate two strings
    var name1 string="PAN ";
    var name2 string ="card";
    var name string=name1+name2;
    fmt.Println(name)

     //To slice the given string by specifying the start and end index
    fmt.Println("The last alphabet of the PAN card number:",pancardNumber[9:10])
    fmt.Println("The numbers in the PAN card number:", pancardNumber[5:9])

    //To display all the characters of the string using for--range
    for i, r := range pancardNumber {
        fmt.Println(string(r),"at",i)
    }
}
