-- MySQL Script generated by MySQL Workbench
-- Mon Nov  6 11:51:09 2017
-- Model: New Model    Version: 1.0
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
  `id_cat` INT NOT NULL AUTO_INCREMENT,
  `name_cat` VARCHAR(30) NOT NULL,
  `cat_short` VARCHAR(10) NULL,
  PRIMARY KEY (`id_cat`),
  UNIQUE INDEX `name_cat_UNIQUE` (`name_cat` ASC),
  UNIQUE INDEX `cat_short_UNIQUE` (`cat_short` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`club`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `almma`.`club` (
  `id_club` INT(4) NOT NULL AUTO_INCREMENT,
  `name_club` VARCHAR(30) NOT NULL,
  `city_club` VARCHAR(25) NULL DEFAULT NULL,
  `trainer_name` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`id_club`),
  UNIQUE INDEX `id_club` (`id_club` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`rank`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `almma`.`rank` (
  `id_rank` INT(1) NOT NULL AUTO_INCREMENT,
  `rank` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`id_rank`),
  UNIQUE INDEX `id_rank` (`id_rank` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`tournament`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `almma`.`tournament` (
  `id_tourn` INT(4) NOT NULL AUTO_INCREMENT,
  `name_tourn` VARCHAR(30) NULL DEFAULT NULL,
  `city_tourn` VARCHAR(25) NOT NULL,
  `date_tourn` DATE NOT NULL,
  `rank_tourn` INT(11) NOT NULL,
  `rank_id_rank` INT(1) NOT NULL,
  PRIMARY KEY (`id_tourn`, `rank_id_rank`),
  UNIQUE INDEX `id_tourn` (`id_tourn` ASC),
  INDEX `fk_tournament_rank1_idx` (`rank_id_rank` ASC),
  CONSTRAINT `fk_tournament_rank1`
    FOREIGN KEY (`rank_id_rank`)
    REFERENCES `almma`.`rank` (`id_rank`)
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
  `id_tourn` INT(4) NOT NULL,
  `id_cat` INT NOT NULL,
  `place` INT(1) NULL DEFAULT NULL,
  `id_player` INT(3) NULL DEFAULT NULL,
  `tournament_id_tourn` INT(4) NOT NULL,
  `category_id_cat` INT NOT NULL,
  PRIMARY KEY (`id_result`, `tournament_id_tourn`, `category_id_cat`),
  INDEX `fk_results_tournament1_idx` (`tournament_id_tourn` ASC),
  INDEX `fk_results_category1_idx` (`category_id_cat` ASC),
  CONSTRAINT `fk_results_tournament1`
    FOREIGN KEY (`tournament_id_tourn`)
    REFERENCES `almma`.`tournament` (`id_tourn`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_results_category1`
    FOREIGN KEY (`category_id_cat`)
    REFERENCES `almma`.`category` (`id_cat`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `almma`.`weight_cat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `almma`.`weight_cat` (
  `id_weight` INT NOT NULL AUTO_INCREMENT,
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
  `id_weight` INT NOT NULL,
  `id_club` INT(3) NOT NULL,
  `id_cat` INT NOT NULL,
  `club_id_club` INT(4) NOT NULL,
  `category_id_cat` INT NOT NULL,
  `results_id_result` INT NOT NULL,
  `results_tournament_id_tourn` INT(4) NOT NULL,
  `weight_cat_id_weight` INT NOT NULL,
  PRIMARY KEY (`id_p`, `club_id_club`, `category_id_cat`, `results_id_result`, `results_tournament_id_tourn`, `weight_cat_id_weight`),
  UNIQUE INDEX `id_p` (`id_p` ASC),
  INDEX `fk_player_club1_idx` (`club_id_club` ASC),
  INDEX `fk_player_category1_idx` (`category_id_cat` ASC),
  INDEX `fk_player_results1_idx` (`results_id_result` ASC, `results_tournament_id_tourn` ASC),
  INDEX `fk_player_weight_cat1_idx` (`weight_cat_id_weight` ASC),
  CONSTRAINT `fk_player_club1`
    FOREIGN KEY (`club_id_club`)
    REFERENCES `almma`.`club` (`id_club`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_player_category1`
    FOREIGN KEY (`category_id_cat`)
    REFERENCES `almma`.`category` (`id_cat`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_player_results1`
    FOREIGN KEY (`results_id_result` , `results_tournament_id_tourn`)
    REFERENCES `almma`.`results` (`id_result` , `tournament_id_tourn`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_player_weight_cat1`
    FOREIGN KEY (`weight_cat_id_weight`)
    REFERENCES `almma`.`weight_cat` (`id_weight`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 12
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
