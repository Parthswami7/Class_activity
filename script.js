class student{
    constructor (name,year)
    {this.name = name;
        this.year = year;
    }
age() {let date = new Date();}  
}
student1 = new student(Parth,2011)
age() {

    let currentYear = new Date().getFullYear();

    return currentYear - this.year;

}

}

// Create one student object

const student1 = new Student("Akansha", 2019);

document.getElementById("student1").innerHTML =

"My name is " + student1.name +

    ". I joined in " + student1.year +

    ". My age is " + student1.age() + ".";