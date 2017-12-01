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
CREATE TABLE IF NOT EXISTS `almma`.`category` (
  `id_cat` INT NOT NULL,
  `name_cat` VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (`id_cat`),
  UNIQUE INDEX `id_cat` (`id_cat` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`club`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `almma`.`club` (
  `id_club` INT(4) NOT NULL AUTO_INCREMENT,
  `name_club` VARCHAR(30) NOT NULL,
  `city_club` VARCHAR(25) NULL DEFAULT NULL,
  `trainer_name` VARCHAR(40) NULL DEFAULT NULL,
  PRIMARY KEY (`id_club`),
  UNIQUE INDEX `id_club` (`id_club` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`weight_cat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `almma`.`weight_cat` (
  `id_weight` INT NOT NULL,
  `value_weight` VARCHAR(4) NOT NULL,
  UNIQUE INDEX `value_weight` (`value_weight` ASC),
  PRIMARY KEY (`id_weight`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`player`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `almma`.`player` (
  `id_p` INT(3) NOT NULL AUTO_INCREMENT,
  `name_p` VARCHAR(25) NOT NULL,
  `last_name_p` VARCHAR(40) NOT NULL,
  `weight` INT NOT NULL,
  `id_club` INT(3) NOT NULL,
  `id_cat` INT NOT NULL,
  PRIMARY KEY (`id_p`, `id_cat`, `id_club`, `weight`),
  UNIQUE INDEX `id_p` (`id_p` ASC),
  INDEX `fk_player_club1_idx` (`id_club` ASC),
  INDEX `fk_player_category1_idx` (`id_cat` ASC),
  INDEX `fk_player_weight_cat1_idx` (`weight` ASC),
  CONSTRAINT `fk_player_club1`
    FOREIGN KEY (`id_club`)
    REFERENCES `almma`.`club` (`id_club`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_player_category1`
    FOREIGN KEY (`id_cat`)
    REFERENCES `almma`.`category` (`id_cat`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_player_weight1`
    FOREIGN KEY (`weight`)
    REFERENCES `almma`.`weight_cat` (`id_weight`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 12
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`tournament`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `almma`.`tournament` (
  `id_tourn` INT(4) NOT NULL AUTO_INCREMENT,
  `name_tourn` VARCHAR(30) NULL,
  `city_tourn` VARCHAR(25) NOT NULL,
  `date_tourn` DATE NOT NULL,
  `rank_tourn` INT(11) NOT NULL,
  PRIMARY KEY (`id_tourn`),
  UNIQUE INDEX `id_tourn` (`id_tourn` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`rank`
-- -----------------------------------------------------
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
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`results`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `almma`.`results` (
  `id_result` INT NOT NULL AUTO_INCREMENT,
  `id_player` INT(3) NOT NULL,
  `id_tourn` INT(4) NOT NULL,
  `place` INT(1) NULL,
  PRIMARY KEY (`id_result`, `id_player`, `id_tourn`),
  INDEX `fk_results_tournament1_idx` (`id_tourn` ASC),
  INDEX `fk_results_player1_idx` (`id_player` ASC),
  CONSTRAINT `fk_results_tournament1`
    FOREIGN KEY (`id_tourn`)
    REFERENCES `almma`.`tournament` (`id_tourn`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_results_player1`
    FOREIGN KEY (`id_player`)
    REFERENCES `almma`.`player` (`id_p`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`fight_field`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `almma`.`fight_field` (
  `id_fight_field` INT NOT NULL,
  `fight_field_name` VARCHAR(25) NULL,
  `fight_field_fight_no` INT NULL,
  PRIMARY KEY (`id_fight_field`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `almma`.`fight`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `almma`.`fight` (
  `id_fight` INT NOT NULL AUTO_INCREMENT,
  `id_p_blue` INT NOT NULL,
  `id_p_red` INT NOT NULL,
  `fight_field_id_fight_field` INT NOT NULL,
  PRIMARY KEY (`id_fight`, `fight_field_id_fight_field`),
  INDEX `fk_fight_fight_field1_idx` (`fight_field_id_fight_field` ASC),
  CONSTRAINT `fk_fight_fight_field1`
    FOREIGN KEY (`fight_field_id_fight_field`)
    REFERENCES `almma`.`fight_field` (`id_fight_field`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `almma`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `almma`.`user` (
  `id_user` INT NOT NULL,
  `login` VARCHAR(45) NOT NULL,
  `user_group` INT NOT NULL,
  `pass` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_user`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
