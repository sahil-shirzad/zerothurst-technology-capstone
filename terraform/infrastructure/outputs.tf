output "vpc_name" {
  value = google_compute_network.securetrack_vpc.name
}

output "cloudsql_name" {
  value = google_sql_database_instance.postgres.name
}
