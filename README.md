# docker-python

Personal practice environment for docker use.



イメージの作成とbuild
```
docker compose up -d --build
```
実際に開ける


docker compose exec python3 bash


インストールコマンドは `gem install hoge` です


```ruby:sushi.rb
def sushi
puts 'お寿司'
end
```