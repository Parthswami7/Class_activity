class Student {
    constructor(name) {
        this.studentname = name;
    }

    // Static method (called on the class, not instance)
    static hello() {
        return "Hello!!";
    }

    // Static method that takes an object as parameter
    static welcome(x) {
        return "Welcome " + x.studentname;
    }

    // Instance method (called on an object)
    hi() {
        return "Hi " + this.studentname;
    }
}

// Create an object
let myname = new Student("Carol");

// Call static method on class
document.getElementById("hello").innerHTML = Student.hello();

// Call instance method on object
document.getElementById("hi").innerHTML = myname.hi();

// Call static method with object as argument
document.getElementById("welcome").innerHTML = Student.welcome(myname);