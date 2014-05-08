jekyll build
cd _site
rm -r *
cd ..
git add *
git commit -m "changed website"
git push origin master