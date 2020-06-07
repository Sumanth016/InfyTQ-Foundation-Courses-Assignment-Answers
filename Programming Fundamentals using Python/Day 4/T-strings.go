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

/*
Length of the PAN card number: 10
PAN card
The last alphabet of the PAN card number: H
The numbers in the PAN card number: 6715
A at 0
A at 1
B at 2
G at 3
T at 4
6 at 5
7 at 6
1 at 7
5 at 8
H at 9
*/
