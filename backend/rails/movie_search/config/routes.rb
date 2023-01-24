Rails.application.routes.draw do

  root "shows#index"

  resources :shows

  get "/boom", to: "shows#boom"

  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
end
