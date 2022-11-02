# frozen_string_literal: true

class AdduserToOfertclases < ActiveRecord::Migration[5.1]
  def change
    add_column :ofertclases, :user, :string
  end
end
