
public class StringToInteger {

	public static void main(String[] args) {
		/* read input from the command line*/ 
		String input = args[0];
		int output = 0;
		
		/* Read a character and check its ascii value if its a 
		  digit then get the numeric value and convert into
		  a decimal number*/
		int sign = 1;
		int i = 0;
		if(input.charAt(0) == '-'){
			sign = -1;
			i++;
		}
		for(i =1; i < input.length(); i++){
			
			char ch = input.charAt(i);
			
			if(ch < 48 || ch > 57 ){
				System.out.println("Undesirable character found");
				return;
			}else{
				int ch_val = ch - '0';
				output = output * 10 + ch_val; 
			}
		}
		output = sign * output;
		
		System.out.println(output);

	}

}
