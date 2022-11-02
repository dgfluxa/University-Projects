# frozen_string_literal: true

class AddCourseToPublicacion < ActiveRecord::Migration[5.1]
  def change
    remove_column :publicacions, :course, :string
    add_reference :publicacions, :course, index: true
  end
end
