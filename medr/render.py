from jinja2 import render_template
from api import product
from api import variant
from api import target
from api import drug

def render(sample_variants,product_name,report_template):
    
    product_info = product.get(product)
    
    variants_ids = product_info["variantids"]

    variant_infos = {}

    for variantid in variants_ids:
        variant_info = variant.get(variantid)
        target_id = variant_info["targetid"]
        target_info = target.get(target_id)
        drugids = target_info["drugids"]
        for drugid in drugids:
            druginfo = drug.get(drugid)
            
    htmlout = render_template(report_template,**variant_infos)

    
