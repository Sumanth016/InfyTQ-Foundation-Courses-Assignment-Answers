//Creating a string
var pancardNumber="AABGT6715H";
//Length of the string
console.log("Length of the PAN card number: " + pancardNumber.length);

//Concatenating two strings
var name1="PAN ";
var name2="card";
var name=name1+name2;
console.log(name);

//Iterating through the string
for (i=0;i < pancardNumber.length;i++)
{
   console.log(pancardNumber[i]);
}

//Slicing a string
console.log("The numbers in the PAN card number: "+pancardNumber.slice(5,9));
