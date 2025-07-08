resource "aws_cloudwatch_event_rule" "lambda_schedule" {
  name                = "run-twitter-bot-schedule"
  description         = "Run Twitter bot on a schedule"
  schedule_expression = "cron(0 */2 * * ? *)"  # every hour
}

resource "aws_cloudwatch_event_target" "lambda_target" {
  rule      = aws_cloudwatch_event_rule.lambda_schedule.name
  target_id = "twitter-bot-lambda"
  arn       = aws_lambda_function.my_lambda.arn
}

resource "aws_lambda_permission" "allow_eventbridge" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.my_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.lambda_schedule.arn
}
