# frozen_string_literal: true

require 'test_helper'

class ProfessorCoursesControllerTest < ActionDispatch::IntegrationTest
  test 'should get update' do
    get professor_courses_update_url
    assert_response :success
  end
end
