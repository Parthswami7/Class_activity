class Student {
    constructor(name, year) {
        this.name = name;   // assign name to the object
        this.year = year;   // assign year to the object
    }

    age() {
        let currentYear = new Date().getFullYear();
        return currentYear - this.year;
    }
}

const student1 = new Student("Parth", 2011);

document.getElementById("student1").innerHTML =
    "My name is " + student1.name +
    ". I was born in " + student1.year +
    ". My age is " + student1.age() + ".";