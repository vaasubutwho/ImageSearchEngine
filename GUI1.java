import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class GUI1{
    private JLabel statusLabel;
    public GUI1(){
        prepareGUI();
    }
    public void prepareGUI(){
        JFrame mainFrame=new JFrame("hello");
        JButton okayButton=new JButton();
        mainFrame.setLayout(new GridLayout(3,1));
        statusLabel=new JLabel("Hello", JLabel.CENTER);
        JLabel headerLabel=new JLabel("", JLabel.CENTER);
        JPanel panel=new JPanel();
        panel.setBackground(Color.MAGENTA);
        okayButton.addActionListener(new MyActionListener());
        mainFrame.add(panel);
        mainFrame.add(okayButton);
        mainFrame.add(statusLabel);
        mainFrame.add(headerLabel);
        mainFrame.setDefaultCloseOperation(mainFrame.EXIT_ON_CLOSE);
        mainFrame.setSize(500, 500);
        mainFrame.setVisible(true);
    }
    class MyActionListener implements ActionListener{
        public void actionPerformed(ActionEvent ae){
            statusLabel.setText("Button Clicked");
        }
    }
    public static void main(String agrs[]){
        new GUI1();
    }
}