jekyll build
cp _site/sitemap.xml sitemap.xml
cd _site
rm -r *
cd ..
git add *
git commit -m "changed website"
git push origin master

