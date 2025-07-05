# cost/cost_model.py

# Simplified static cost model (USD/month)
COST_MAP = {
    "aws_instance": {
        "t2.micro": 8,
        "t3.micro": 8,
        "t3.medium": 20,
        "t3.large": 40,
        "default": 15  # fallback
    },
    "aws_s3_bucket": 0.023 * 50,  # assuming 50 GB average per bucket
    "aws_db_instance": {
        "db.t3.micro": 15,
        "db.t3.medium": 40,
        "default": 25
    },
    "aws_ebs_volume": 0.10 * 100,  # assuming 100 GB
    "aws_elb": 20,
    "aws_alb": 25
}


def get_resource_cost(resource_type, attributes=None):
    if resource_type not in COST_MAP:
        return 0

    pricing = COST_MAP[resource_type]

    # If pricing is a flat number
    if isinstance(pricing, (int, float)):
        return pricing

    # If pricing is a dict (e.g., EC2 or RDS types)
    if isinstance(pricing, dict):
        key = None

        # Try to extract instance_class or instance_type
        if attributes:
            key = attributes.get("instance_type") or attributes.get("instance_class")

        return pricing.get(key, pricing.get("default", 0))

    return 0
