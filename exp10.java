import java.security.MessageDigest;
import java.util.Scanner;
public class SHA1Hash {
    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter text to hash using SHA-1: ");
            String input = sc.nextLine();
            // Create SHA-1 object
            MessageDigest md = MessageDigest.getInstance("SHA-1");
            // Generate hash
            byte[] digest = md.digest(input.getBytes());
            // Convert to hex
            StringBuilder hash = new StringBuilder();
            for (byte b : digest) {
                hash.append(String.format("%02X", b));
            }
            // Output
            System.out.println("SHA-1 Hash: " + hash);
            sc.close();
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
