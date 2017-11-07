import javax.swing.*;
import java.awt.Choice;
import java.awt.Color;
import java.awt.event.*;

public class Viewer {

	public static void main(String[] args) {
		
		int i_fight_nmbr = 0;

		// create graphic elements
		
		JFrame f_main = new JFrame("Almma Player Viewer");
		JFrame f_viewer = new JFrame("Almma Player Viewer");
		JFrame f_mini_viewer = new JFrame("Podgl¹d");
		
		JLabel lbl_red = new JLabel("Czerwony zawodnik");
		JLabel lbl_blue = new JLabel("Niebieski zawodnik");
		JLabel lab_octagon = new JLabel("Pole Walki");
		JLabel lbl_weight = new JLabel("Waga");
		JLabel lbl_category = new JLabel("Kategoria");
		JLabel lbl_fight_nmbr = new JLabel("Numer walki");
		JLabel lbl_fight_nmbr_show = new JLabel(String.valueOf(i_fight_nmbr));
		
		JTextField tf_red = new JTextField();
		JTextField tf_blue = new JTextField();

		Choice category = new Choice();
		category.add("Junior");
		category.add("PK");
		category.add("OFS");
		category.add("FC");
		category.add("M³odzie¿owiec");
		
		Choice weight = new Choice();
		weight.add("55");
		weight.add("61");
		weight.add("66");
		weight.add("70");
		weight.add("77");
		weight.add("84");
		weight.add("93");
		weight.add("93+");
		
		Choice octagon = new Choice();
		octagon.add("Octagon 1");
		octagon.add("Octagon 2");
		octagon.add("Octagon 3");
		octagon.add("Mata 1");
		octagon.add("Mata 2");
		octagon.add("Mata 3");
		octagon.add("Mata ¯ó³ta");
		octagon.add("Mata Niebieska");
		octagon.add("Mata Czerwona");
		octagon.add("Mata Œrodkowa");
		
		JButton btn_show = new JButton("Poka¿");
		JButton bnt_pluse = new JButton(" + ");
		JButton bnt_minus = new JButton(" - ");
		JButton btn_start = new JButton("START");
		JButton btn_pause = new JButton("STOP");
		JButton btn_reset = new JButton("Reset");
		JButton btn_play_off = new JButton("Dogrywka");
		
		JCheckBox fight_finished = new JCheckBox("Walka zakoñczona");
		
		//layout
		f_main.setVisible(true);
		f_main.setSize(1200, 600);
		f_main.setLayout(null);
		f_main.setBackground(Color.CYAN);
		
		f_viewer.setVisible(false);
		f_viewer.setSize(1600, 800);
		f_viewer.setLayout(null);
		
		f_mini_viewer.setVisible(false);
		f_mini_viewer.setSize(600, 400);
		f_mini_viewer.setLayout(null);
		
		f_main.add(fight_finished);
		f_main.add(lbl_blue);
		f_main.add(lab_octagon);
		f_main.add(lbl_category);
		f_main.add(lbl_fight_nmbr);
		f_main.add(lbl_fight_nmbr_show);
		f_main.add(lbl_red);
		f_main.add(lbl_weight);
		f_main.add(tf_blue);
		f_main.add(tf_red);
		f_main.add(category);
		f_main.add(weight);
		f_main.add(octagon);
		f_main.add(bnt_minus);
		f_main.add(bnt_pluse);
		f_main.add(btn_pause);
		f_main.add(btn_play_off);
		f_main.add(btn_reset);
		f_main.add(btn_show);
		f_main.add(btn_start);
		f_main.add(fight_finished);
		

		
		
		
		
		
	}
	
}
