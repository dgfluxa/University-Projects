# frozen_string_literal: true

require 'test_helper'

class StudentCoursesControllerTest < ActionDispatch::IntegrationTest
  test 'should get update' do
    get student_courses_update_url
    assert_response :success
  end
end
