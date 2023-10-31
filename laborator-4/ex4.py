def build_xml_element(tag, content, **attributes):
    opening_tag = f"<{tag}"
    for key, value in attributes.items():
        opening_tag += f' {key}="{value}"'
    opening_tag += ">"

   
    closing_tag = f"</{tag}>"
    
    xml_element = f"{opening_tag}{content}{closing_tag}"

    return xml_element


xml_element = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(xml_element)
