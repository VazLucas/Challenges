import java.util.*;

public class Application3 {

    public static void main(String[] args) {

        Scanner source = new Scanner(System.in);
        int result = 0;
        List<Integer> results = new ArrayList<>();
        int k = 1;

        while (source.hasNext()) {

            int operandsQuantity = source.nextInt();

            if (operandsQuantity < 1 || operandsQuantity > 100) {
                break;
            }
            if (operandsQuantity != 0) {
                String equation = source.next();

                String equationFormatted = equation.replaceAll("[0-9]", "");
                ArrayList equationCounter = new ArrayList<>((List.of(equation.split("[^0-9]"))));
                ArrayList equationOperator = new ArrayList<>();
                equationOperator.add("");
                for (int i = 0; i < equationFormatted.length(); i++) {
                    equationOperator.add(equationFormatted.charAt(i));
                }
                if (operandsQuantity < equationCounter.size()) {
                    System.out.println("Exceeded number of operands, you must have inserted " + operandsQuantity + " operands");

                } else if (operandsQuantity > equationCounter.size()) {
                    System.out.println("You must have inserted " + operandsQuantity + " operands");

                } else {
                    for (int j = 0; j < equationCounter.size(); j++) {
                        if (equationOperator.get(j).hashCode() == "-".hashCode()) {

                            result = result - Integer.parseInt((String) equationCounter.get(j));

                        } else {
                            result = Integer.parseInt((String) equationCounter.get(j)) + result;
                        }

                    }
                    results.add(result);
                }
            }


            result = 0;
        }
            for (int i : results) {
                System.out.println("Test: " + k);
                System.out.println(i);
                k++;
        }
    }
}