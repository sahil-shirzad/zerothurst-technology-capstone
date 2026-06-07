provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_cloud_run_v2_service" "securetrack" {
  name     = "securetrack-app"
  location = var.region

  template {
    containers {
      image = var.container_image

      ports {
        container_port = 8080
      }
    }
  }
}

resource "google_cloud_run_service_iam_member" "public" {
  service  = google_cloud_run_v2_service.securetrack.name
  location = var.region
  role     = "roles/run.invoker"
  member   = "allUsers"
}
