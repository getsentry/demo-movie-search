class ShowsController < ApplicationController
  def index
      @shows = Show.all
  end

  def show
      @show = Show.find(params[:id])
  end

  def boom
      raise "Boom!"
  end
end
