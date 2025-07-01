provider "aws" {
  region = "us-east-1"
}

resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_basic_exec" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "my_lambda" {
  function_name = "twitter_bot_lambda"
  description   = "A Lambda function to run the Twitter bot"
  runtime       = "python3.11"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "twitter_bot_lambda.lambda_handler"
  filename      = "lambda_function.zip"
  source_code_hash = filebase64sha256("lambda_function.zip")

  timeout = 10
  environment {
    variables = {
      AWS_ACCESS_KEY_ID     = var.AWS_ACCESS_KEY_ID
      AWS_SECRET_ACCESS_KEY = var.AWS_SECRET_ACCESS_KEY
      BEARER_TOKEN          = var.BEARER_TOKEN
      CONSUMER_KEY          = var.CONSUMER_KEY
      CONSUMER_SECRET       = var.CONSUMER_SECRET
      TWITTER_ACCESS_TOKEN  = var.TWITTER_ACCESS_TOKEN
      TWITTER_ACCESS_TOKEN_SECRET = var.TWITTER_ACCESS_TOKEN_SECRET
      OPEN_AI_API_KEY       = var.OPEN_AI_API_KEY
    }
  }
}
