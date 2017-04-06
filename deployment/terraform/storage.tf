resource "aws_s3_bucket" "training-results" {
  bucket = "raster-vision-${lower("${var.environment}")}-training-results-${var.aws_region}"
  acl    = "private"

  cors_rule {
    allowed_origins = ["*"]
    allowed_methods = ["GET"]
    max_age_seconds = 3000
    allowed_headers = ["Authorization"]
  }

  tags {
    Environment = "${var.environment}"
    Project     = "${var.project}"
  }
}

resource "aws_s3_bucket" "training-jobs" {
  bucket = "raster-vision-${lower("${var.environment}")}-training-jobs-${var.aws_region}"
  acl    = "private"

  tags {
    Environment = "${var.environment}"
    Project     = "${var.project}"
  }
}
