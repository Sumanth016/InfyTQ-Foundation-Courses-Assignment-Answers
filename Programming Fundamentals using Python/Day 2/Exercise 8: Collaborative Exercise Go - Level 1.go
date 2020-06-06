package main
import ("fmt")
func main(){
    var finalFee float32
    //Write your program logic here
    //Populate the variable: finalFee
    var course_fee float32=25000
    var extra_fee float32=1500
    var marks float32=70
    var percentage float32=(marks/2)/100
    var scholarship_amount float32= percentage*course_fee
    finalFee=course_fee-scholarship_amount+extra_fee
     //Do not modify the below print statement for verification to work
     fmt.Println(finalFee) 
}
