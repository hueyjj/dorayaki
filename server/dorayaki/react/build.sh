#!/usr/bin/env bash
if [ "$#" -ne 1 ]; then
    echo "No argument provided"
    exit 1
fi

react_entry_filename=$1
if [ ! -f "src/$react_entry_filename.tsx" ]; then
    echo "$react_entry_filename.tsx doesn't exist."
    exit 1
fi
echo "Found src/$react_entry_filename.tsx"

cp src/$react_entry_filename.tsx src/index.tsx
echo "Replaced src/index.tsx with src/$react_entry_filename.tsx"

yarn_build="yarn build"
$yarn_build

# Django static files directory
django_static_dir=build_django_static
react_static_dir=$django_static_dir/react_$react_entry_filename
if [ ! -d $react_static_dir ]; then
    mkdir -p $react_static_dir
    echo "Created $react_static_dir directory"
fi
echo "Found Django static files directory at $react_static_dir"

if [ ! -d "build/static" ]; then
    echo "Couldn't find build/static. Check $yarn_build for errors."
    exit 1
fi

cp -r build/static/* $react_static_dir 
echo "Copied contents of build/static to $react_static_dir"

pushd $django_static_dir > /dev/null
echo "Entered $django_static_dir directory"

# Build a django template for javascript files
js_template="react_$react_entry_filename/js.html"
cat << EOF > $js_template
{% load static %}
EOF

for js in "react_$react_entry_filename/js/"*.js
do
    echo '<script src="{% static '\'$js\'' %}"></script>' >> $js_template
    echo "Appended $js as script tag to $js_template"
done

# Build a django template for css files
css_template="react_$react_entry_filename/css.html"
cat << EOF > $css_template
{% load static %}
EOF

for css in "react_$react_entry_filename/css/"*.css
do
    echo '<link rel="stylesheet" href="{% static '\'$css\'' %}"></link>' >> $css_template
    echo "Appended $css as link tag to $css_template"
done

popd > /dev/null
echo "Exited build_django_static directory"

# Django template files directory
build_django_template_dir=build_django_template/react_$react_entry_filename
if [ ! -d $build_django_template_dir ]; then
    mkdir -p $build_django_template_dir
    echo "Created $react_static_dir directory"
fi
echo "Found Django template files directory at $build_django_template_dir"

mv $react_static_dir/js.html $build_django_template_dir
mv $react_static_dir/css.html $build_django_template_dir
echo "Moved Django js and css templates to $build_django_template_dir"
