provider "google" {
  project = var.project_id
  region  = var.region
}

# VPC

resource "google_compute_network" "securetrack_vpc" {
  name                    = "securetrack-vpc"
  auto_create_subnetworks = true
}

# Cloud SQL

resource "google_sql_database_instance" "postgres" {
  name             = "securetrack-db"
  region           = var.region
  database_version = "POSTGRES_15"

  settings {
    tier = "db-f1-micro"
  }
}

# Secret Manager

resource "google_secret_manager_secret" "db_password" {
  secret_id = "db-password"

  replication {
    auto {}
  }
}
