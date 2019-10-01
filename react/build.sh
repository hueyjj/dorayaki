#!/usr/bin/env bash

if [ "$#" -ne 1 ]; then
    echo "No argument provided"
    exit 1
fi
echo "Script started"
name=$1
echo "Argument provided: $name"

build_dir=build_django_static_files/$name
echo "Creating $build_dir directory"
mkdir -p $build_dir

if [ ! -d "build/static" ]; then
    echo "build/static doesn't exist"
    echo "Exiting script..."
    exit 1
fi

echo "Copying contents of build/static to $build_dir"
cp -r build/static/* $build_dir

pushd build_django_static_files > /dev/null
echo "Entered build_django_static_files directory"

# Build a django template for javascript files
js_django_html_template="$name/$name.js".html
cat << EOF > $js_django_html_template
{% load static %}
EOF

for js in "$name/js/"*.js
do
    echo "Appending $js as script tag to $js_django_html_template"
    echo '<script src="{% static '\'$js\'' %}"></script>' >> $js_django_html_template
done

# Build a django template for css files
css_django_html_template="$name/$name.css".html
cat << EOF > $css_django_html_template
{% load static %}
EOF

for css in "$name/css/"*.css
do
    echo "Appending $css as link tag to $css_django_html_template"
    echo '<link rel="stylesheet" href="{% static '\'$css\'' %}"></link>' >> $css_django_html_template
done

popd > /dev/null
echo "Exited build_django_static_files directory"