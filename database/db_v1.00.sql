-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema almma
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema almma
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `almma` DEFAULT CHARACTER SET utf8 ;
USE `almma` ;

-- -----------------------------------------------------
-- Table `almma`.`category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `almma`.`category` ;

CREATE TABLE IF NOT EXISTS `almma`.`category` (
  `id_cat` INT(11) NOT NULL,
  `name_cat` VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (`id_cat`),
  UNIQUE INDEX `id_cat` (`id_cat` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`club`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `almma`.`club` ;

CREATE TABLE IF NOT EXISTS `almma`.`club` (
  `id_club` INT(4) NOT NULL AUTO_INCREMENT,
  `name_club` VARCHAR(50) NULL DEFAULT NULL,
  `city_club` VARCHAR(25) NULL DEFAULT 'Miasto',
  `trainer_name` VARCHAR(40) NULL DEFAULT 'Nazwisko Trenera',
  PRIMARY KEY (`id_club`))
ENGINE = InnoDB
AUTO_INCREMENT = 84
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`weight_cat`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `almma`.`weight_cat` ;

CREATE TABLE IF NOT EXISTS `almma`.`weight_cat` (
  `id_weight` INT(11) NOT NULL,
  `value_weight` VARCHAR(4) NOT NULL,
  PRIMARY KEY (`id_weight`),
  UNIQUE INDEX `value_weight` (`value_weight` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`player`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `almma`.`player` ;

CREATE TABLE IF NOT EXISTS `almma`.`player` (
  `id_p` INT(3) NOT NULL AUTO_INCREMENT,
  `name_p` VARCHAR(25) NOT NULL,
  `last_name_p` VARCHAR(40) NOT NULL,
  `id_weight` INT(11) NOT NULL,
  `id_club` INT(3) NOT NULL,
  PRIMARY KEY (`id_p`, `id_club`, `id_weight`),
  INDEX `fk_player_club1_idx` (`id_club` ASC),
  INDEX `fk_player_weight_cat1_idx` (`id_weight` ASC),
  UNIQUE INDEX `id_p_UNIQUE` (`id_p` ASC),
  CONSTRAINT `fk_player_club1`
    FOREIGN KEY (`id_club`)
    REFERENCES `almma`.`club` (`id_club`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_player_weight1`
    FOREIGN KEY (`id_weight`)
    REFERENCES `almma`.`weight_cat` (`id_weight`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`fight_field`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `almma`.`fight_field` ;

CREATE TABLE IF NOT EXISTS `almma`.`fight_field` (
  `id_fight_field` INT(11) NOT NULL,
  `fight_field_name` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`id_fight_field`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`fight`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `almma`.`fight` ;

CREATE TABLE IF NOT EXISTS `almma`.`fight` (
  `id_fight` INT(11) NOT NULL AUTO_INCREMENT,
  `id_p_blue` INT(11) NOT NULL,
  `id_p_red` INT(11) NOT NULL,
  `fight_field_id_fight_field` INT(11) NOT NULL,
  PRIMARY KEY (`id_fight`),
  INDEX `fk_fight_player1_idx` (`id_p_blue` ASC),
  INDEX `fk_fight_player2_idx` (`id_p_red` ASC),
  INDEX `fk_pole_walki_idx` (`fight_field_id_fight_field` ASC),
  CONSTRAINT `fk_fight_player1`
    FOREIGN KEY (`id_p_blue`)
    REFERENCES `almma`.`player` (`id_p`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_fight_player2`
    FOREIGN KEY (`id_p_red`)
    REFERENCES `almma`.`player` (`id_p`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pole_walki`
    FOREIGN KEY (`fight_field_id_fight_field`)
    REFERENCES `almma`.`fight_field` (`id_fight_field`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`tournament`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `almma`.`tournament` ;

CREATE TABLE IF NOT EXISTS `almma`.`tournament` (
  `id_tourn` INT(4) NOT NULL AUTO_INCREMENT,
  `name_tourn` VARCHAR(30) NULL DEFAULT NULL,
  `city_tourn` VARCHAR(25) NOT NULL,
  `date_tourn` DATE NOT NULL,
  `rank_tourn` INT(11) NOT NULL,
  PRIMARY KEY (`id_tourn`),
  UNIQUE INDEX `id_tourn` (`id_tourn` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`rank`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `almma`.`rank` ;

CREATE TABLE IF NOT EXISTS `almma`.`rank` (
  `id_rank` INT(1) NOT NULL AUTO_INCREMENT,
  `rank` VARCHAR(25) NOT NULL,
  `tournament_id_tourn` INT(4) NOT NULL,
  PRIMARY KEY (`id_rank`, `tournament_id_tourn`),
  UNIQUE INDEX `id_rank` (`id_rank` ASC),
  INDEX `fk_rank_tournament1_idx` (`tournament_id_tourn` ASC),
  CONSTRAINT `fk_rank_tournament1`
    FOREIGN KEY (`tournament_id_tourn`)
    REFERENCES `almma`.`tournament` (`id_tourn`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`results`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `almma`.`results` ;

CREATE TABLE IF NOT EXISTS `almma`.`results` (
  `id_result` INT(11) NOT NULL AUTO_INCREMENT,
  `id_player` INT(3) NOT NULL DEFAULT 0,
  `id_tourn` INT(4) NOT NULL DEFAULT 0,
  `place` INT(1) NULL DEFAULT NULL,
  `id_cat` INT(11) NOT NULL,
  PRIMARY KEY (`id_result`, `id_player`, `id_tourn`, `id_cat`),
  INDEX `fk_results_tournament1_idx` (`id_tourn` ASC),
  INDEX `fk_results_player1_idx` (`id_player` ASC),
  INDEX `fk_results_category1_idx` (`id_cat` ASC),
  CONSTRAINT `fk_results_player1`
    FOREIGN KEY (`id_player`)
    REFERENCES `almma`.`player` (`id_p`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_results_tournament1`
    FOREIGN KEY (`id_tourn`)
    REFERENCES `almma`.`tournament` (`id_tourn`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_results_category1`
    FOREIGN KEY (`id_cat`)
    REFERENCES `almma`.`category` (`id_cat`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `almma`.`user` ;

CREATE TABLE IF NOT EXISTS `almma`.`user` (
  `id_user` INT(11) NOT NULL,
  `login` VARCHAR(45) NOT NULL,
  `user_group` INT(11) NOT NULL,
  `pass` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_user`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`category_has_player`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `almma`.`category_has_player` ;

CREATE TABLE IF NOT EXISTS `almma`.`category_has_player` (
  `category_id_cat` INT(11) NOT NULL,
  `player_id_p` INT(3) NOT NULL,
  PRIMARY KEY (`category_id_cat`, `player_id_p`),
  INDEX `fk_category_has_player_player1_idx` (`player_id_p` ASC),
  INDEX `fk_category_has_player_category1_idx` (`category_id_cat` ASC),
  CONSTRAINT `fk_category_has_player_category1`
    FOREIGN KEY (`category_id_cat`)
    REFERENCES `almma`.`category` (`id_cat`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_category_has_player_player1`
    FOREIGN KEY (`player_id_p`)
    REFERENCES `almma`.`player` (`id_p`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
