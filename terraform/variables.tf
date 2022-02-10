variable "cluster" {
  default = "cluster-name"
}
variable "web-app" {
  type        = string
  description = "Name of application"
  default     = "act-test"
}
variable "zone" {
  default = "us-central1-a"
}
variable "docker-image" {
  type        = string
  description = "name of the docker image to deploy"
  default     = "impavithra/flask-app:v2"
}
variable "ATC_USERNAME" {
  default = "PAVITHRA"
}

variable "ATC_pASSWORD" {
  default = "1234@#abc"
}