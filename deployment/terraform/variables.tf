variable "project" {
  default = "Aerial ML"
}

# Must be one of release, staging, production
variable "environment" {}

variable "aws_key_name" {}

variable "aws_region" {}

variable "aws_vpc_id" {
  default = "vpc-3aa9ab5d"
}

variable "fleet_iam_role_arn" {
  default = "arn:aws:iam::002496907356:role/aws-ec2-spot-fleet-role"
}

variable "fleet_instance_profile" {
  default = "OpenTreeIDInstanceProfile"
}

variable "fleet_spot_price" {
  default = "0.9"
}

variable "fleet_allocation_strategy" {
  default = "lowestPrice"
}

variable "fleet_target_capacity" {
  default = "1"
}

variable "fleet_security_group_id" {
  default = "sg-0ed0cc74"
}

variable "fleet_ami" {
  default = "ami-b1e2c4a6"
}

# VPC
variable "vpc_cidr_block" {}

variable "vpc_private_subnet_cidr_blocks" {
  type = "list"
}

variable "vpc_public_subnet_cidr_blocks" {
  type = "list"
}

variable "vpc_external_access_cidr_block" {}
variable "vpc_bastion_instance_type" {}
variable "vpc_bastion_ami" {}

variable "vpc_availibility_zones" {
  type = "list"
}

# ECS

variable "ecs_instance_ami_id" {}

# Batch ECS Cluster

variable "batch_ecs_cluster_name" {}
variable "batch_container_instance_type" {
  description = "Must be a GPU instance"
}
variable "batch_container_instance_asg_desired_capacity" {}
variable "batch_container_instance_asg_min_size" {}
variable "batch_container_instance_asg_max_size" {}
variable "batch_ecs_engine_task_cleanup_wait_duration" {
  default = "5m"
}
variable "batch_ecs_image_cleanup_interval" {
  default = "10m"
}
variable "batch_ecs_image_minimum_cleanup_age" {
  default = "30m"
}
variable "batch_spot_price" {}
