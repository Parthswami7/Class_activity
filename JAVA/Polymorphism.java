//guess is it runtime or compile time polymorphism 
class Hillstation{
    void location(){
        System.out.println("Location is:");
    }
    void famousfor(){
        System.out.println("Famous for:");
    }

}
class Manali extends Hillstation {
    void location(){
        System.out.println("Manali is in Himachal Pradesh");
    }
    void famousfor(){
        System.out.println("It is famous for Hadimba Temple and adventure sports");
    }
}
class Mussoorie extends Hillstation{
    void location(){
        System.out.println("Mussoorie is in Uttrakhand");
    }
    void famousfor(){
        System.out.println("It is Famous for education institutions");
    }
}
class Gulmarg extends Hillstation {
    void location(){
        System.out.println("Gulmarg is in J&K");
    }
    void famousfor(){
        System.out.println("It is famous for skiing");
    }
}
class Main{
    public static void main(String args[]){
        Hillstation A = new Hillstation();
        Hillstation M = new Manali();

        Hillstation Mu = new Mussoorie();
        
        Hillstation G = new Gulmarg();

        A.location();
        A.famousfor();

        M.location();
        M.famousfor();

        Mu.location();
        Mu.famousfor();

        G.location();
        G.famousfor();
    }
}