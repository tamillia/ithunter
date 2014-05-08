jekyll build
cd _site
rm -r *
cd ..
git add --all
git commit -m "changed website"
git push origin master
