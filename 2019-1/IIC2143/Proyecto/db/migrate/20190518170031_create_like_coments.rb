# frozen_string_literal: true

class CreateLikeComents < ActiveRecord::Migration[5.1]
  def change
    create_table :like_coments do |t|
      t.references :user, foreign_key: true
      t.references :publicacion_comment, foreign_key: true
      t.integer :like

      t.timestamps
    end
  end
end
